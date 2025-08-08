from fastapi import APIRouter, UploadFile, File, HTTPException
from nutrihelp_ai.services.image_pipeline import ImagePipelineService
from nutrihelp_ai.services.nutribot import AgentClass
from nutrihelp_ai.utils.input_formatter import format_chat_input 

router = APIRouter()

@router.post("/image-analysis")
async def full_image_analysis(file: UploadFile = File(...)):
    try:
        # Step 1: Run image through the AI pipeline
        pipeline = ImagePipelineService()
        food_type, calories = await pipeline.process_image(file)

        # Step 2: Format input for Nutribot (LLM generator)
        formatted_input = format_chat_input(food_type, calories)

        # Step 3: Get Nutribot-generated recommendation
        agent = AgentClass()
        recommendation = agent.run_agent(formatted_input)

        # Step 4: Return complete structured response
        return {
            "food": food_type,
            "estimated_calories": calories,
            "recommendation": recommendation
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
